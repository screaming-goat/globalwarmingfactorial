FROM golang:latest
RUN go get github.com/screaming-goat/globalwarmingfactorial/go/server
RUN go install github.com/screaming-goat/globalwarmingfactorial/go/server
ENTRYPOINT /go/bin/server
EXPOSE 36215
