FROM golang:1.21-alpine as build

WORKDIR /go/src/app
ADD . /go/src/app
RUN CGO_ENABLED=0 go build -o /decode-golang -ldflags="-s -w" *.go

FROM alpine:latest as certs
RUN apk --update add ca-certificates

FROM scratch
COPY --from=build /decode-golang /
COPY --from=certs /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/ca-certificates.crt

CMD ["/decode-golang"]
