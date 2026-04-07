.PHONY: build test lint proto clean

BINARY := eebus-bridge
GO := go

build:
	$(GO) build -o bin/$(BINARY) ./cmd/eebus-bridge

test:
	$(GO) test -v -race ./...

lint:
	$(GO) vet ./...

proto:
	buf generate

clean:
	rm -rf bin/
