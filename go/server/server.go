package main

import (
	"log"
	"net"

	"golang.org/x/net/context"
	"google.golang.org/grpc"
	pb "github.com/screaming-goat/globalwarmingfactorial/go/factorial"
)

const (
	address = "localhost:36215"
	port = ":36215"
)

// server is used to implement helloworld.GreeterServer.
type server struct{}

// SayHello implements helloworld.GreeterServer
func (s *server) Factorial(ctx context.Context, in *pb.FactorialRequest) (*pb.FactorialResponse, error) {
	if in.N == 1 {
		return &pb.FactorialResponse{Result: 1}, nil
	}

	conn, err := grpc.Dial(address, grpc.WithInsecure())
	if err != nil {
		log.Fatalf("did not connect: %v", err)
	}
	defer conn.Close()
	c := pb.NewMathServiceClient(conn)

	// Contact the server and print out its response.
	r, err := c.Factorial(context.Background(), &pb.FactorialRequest{N: in.N - 1})
	if err != nil {
		log.Fatalf("could not call factorial: %v", err)
	}

	return &pb.FactorialResponse{Result: in.N * r.Result}, nil
}

func main() {
	lis, err := net.Listen("tcp", port)
	if err != nil {
		log.Fatalf("failed to listen: %v", err)
	}
	s := grpc.NewServer()
	pb.RegisterMathServiceServer(s, &server{})
	if err := s.Serve(lis); err != nil {
		log.Fatalf("failed to serve: %v", err)
	}
}
