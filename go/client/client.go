package main

import (
	"log"
	"flag"


	"golang.org/x/net/context"
	"google.golang.org/grpc"
	pb "github.com/screaming-goat/globalwarmingfactorial/go/factorial"
)

func main() {
	var serverflag = flag.String("server", "localhost:36215", "factorial server")
	var nflag = flag.Int64("n", 1, "input value to factorial function")

	flag.Parse()

	// Set up a connection to the server.
	conn, err := grpc.Dial(*serverflag, grpc.WithInsecure())
	if err != nil {
		log.Fatalf("did not connect: %v", err)
	}
	defer conn.Close()
	c := pb.NewMathServiceClient(conn)

  var n uint64 = uint64(*nflag)

	r, err := c.Factorial(context.Background(), &pb.FactorialRequest{N: n})
	if err != nil {
		log.Fatalf("could not call factorial: %v", err)
	}
	log.Printf("Factorial of %d is %d", n, r.Result)
}
