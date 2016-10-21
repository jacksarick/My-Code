use std::env;

fn fib(n: i32) -> i32 {
	if n <= 2 {
		1
	}

	else {
		fib(n - 1) + fib(n - 2)
	}
}

fn main() {
	let args: Vec<String> = env::args().collect();
	let num = args[1].parse::<i32>().unwrap();
    println!("{}th fibonacci number: {}", num, fib(num ));
}