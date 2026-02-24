import argparse

parser = argparse.ArgumentParser(description = "Simple Calculator")
parser.add_argument("num1", type="float", help="Number 1")
parser.add_argument("num2", type="float", help="Number 2")
parser.add_argument("operation", choices=["add", "sub", "mul", "div"], help="Number 2")

args = parser.parse_args()

match(args.operation):
    case "add":
        print(f"The result is {args.num1 + args.num2}")


