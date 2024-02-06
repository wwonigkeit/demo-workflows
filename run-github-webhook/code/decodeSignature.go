package main

import (
	"crypto/hmac"
	"crypto/sha1"
	"flag"
	"fmt"
	"os"
)

// IsValidPayload checks if the github payload's hash fits with
// the hash computed by GitHub sent as a header
func IsValidPayload(secret, headerHash string, payload []byte) bool {
	hash := HashPayload(secret, payload)
	return hmac.Equal(
		[]byte(hash),
		[]byte(headerHash),
	)
}

// HashPayload computes the hash of payload's body according to the webhook's secret token
// see https://developer.github.com/webhooks/securing/#validating-payloads-from-github
// returning the hash as a hexadecimal string
func HashPayload(secret string, playloadBody []byte) string {
	hm := hmac.New(sha1.New, []byte(secret))
	hm.Write(playloadBody)
	sum := hm.Sum(nil)
	return fmt.Sprintf("%x", sum)
}

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func main() {
	secretPtr := flag.String("secret", "secret", "GitHub shared secret")
	headerPtr := flag.String("header", "header", "GitHub header hash")
	payloadPtr := flag.String("payload", "payload", "GitHub webhook payload as a JSON file path i.e. dir/payload.json")

	flag.Parse()

	dat, err := os.ReadFile(*payloadPtr)
	check(err)
	// fmt.Print(string(dat))

	fmt.Println("Valid:", IsValidPayload(*secretPtr, *headerPtr, dat))
	fmt.Println("HashPayload:", HashPayload(*secretPtr, dat))
	//fmt.Println("IsValidPayload:", *secretPtr, *headerPtr, *payloadPtr)
	//fmt.Println("HashPayload:", *secretPtr, *payloadPtr)

}
