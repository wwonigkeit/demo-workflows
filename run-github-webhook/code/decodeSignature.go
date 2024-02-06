package main

import (
	"context"
	"crypto/hmac"
	"crypto/sha256"
	"encoding/hex"
	"fmt"
	"io"
	"net/http"
	"os"
	"os/signal"
	"strings"
	"syscall"
	"time"
)

const (
	DirektivActionIDHeader     = "Direktiv-ActionID"
	DirektivErrorCodeHeader    = "Direktiv-ErrorCode"
	DirektivErrorMessageHeader = "Direktiv-ErrorMessage"
)

const code = "io.direktiv.github.validator-%s.error"

func main() {

	mux := http.NewServeMux()
	fmt.Printf("Starting validator server listening on :8080\n")
	mux.HandleFunc("/", WebhookHandler)

	srv := &http.Server{
		Addr:    ":8080",
		Handler: mux,
	}

	fmt.Printf("Listening on :8080\n")

	sigs := make(chan os.Signal, 1)
	signal.Notify(sigs, syscall.SIGTERM)

	go func() {
		<-sigs
		shutdown(srv)
	}()

	srv.ListenAndServe()
}

// WebhookHandler handles GitHub webhook requests
func WebhookHandler(w http.ResponseWriter, r *http.Request) {
	aid := r.Header.Get(DirektivActionIDHeader)
	log(aid, "Received webhook request for validation")

	if r.Method != http.MethodPost {
		respondWithErr(w, fmt.Sprintf(code, "methoderr"), "Method Not Allowed")
		return
	}
	body, err := io.ReadAll(r.Body)
	if err != nil {
		respondWithErr(w, fmt.Sprintf(code, "bodyerr"), err.Error())
		return
	}

	signatureHeader := r.Header.Get("X-Hub-Signature-256")
	if ValidateSignature(w, body, signatureHeader) {
		log(aid, "Payload Validated")
		marshalBytes := []byte(`{"result": "Payload Validated"}`)
		respond(w, marshalBytes)
	} else {
		log(aid, "Unauthorized - Signature Mismatch")
		respondWithErr(w, fmt.Sprintf(code, "invalidsiganture"), "Unauthorized - Signature Mismatch")
	}
}

// ValidateSignature validates the GitHub webhook signature
func ValidateSignature(w http.ResponseWriter, body []byte, signatureHeader string) bool {
	if signatureHeader == "" || len(signatureHeader) < 7 {
		respondWithErr(w, fmt.Sprintf(code, "invalidheader"), "Invalid signature header")
		return false
	}

	fmt.Println("Validating signature...")

	// secret := os.Getenv("WEBHOOK_SECRET")
	secret := "api123"

	computedHash := hmac.New(sha256.New, []byte(secret))
	computedHash.Write(body)
	expectedSig := hex.EncodeToString(computedHash.Sum(nil))

	return hmac.Equal([]byte(expectedSig), []byte(signatureHeader[7:]))
}

func shutdown(srv *http.Server) {
	ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
	defer cancel()
	srv.Shutdown(ctx)
}

func log(aid, l string) {
	if aid == "development" || aid == "Development" {
		fmt.Println(l)
	} else {
		http.Post(fmt.Sprintf("http://localhost:8889/log?aid=%s", aid), "plain/text", strings.NewReader(l))
	}
}

func respond(w http.ResponseWriter, data []byte) {
	w.Header().Add("Content-Type", "application/json")
	w.Write(data)
}

func respondWithErr(w http.ResponseWriter, code, err string) {
	w.Header().Set(DirektivErrorCodeHeader, code)
	w.Header().Set(DirektivErrorMessageHeader, err)
	w.WriteHeader(http.StatusInternalServerError)
	w.Write([]byte(err))
}
