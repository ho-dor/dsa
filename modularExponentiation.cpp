#include <bits/stdc++.h>

int modularExponentiation(int x, int n, int m) {
	// Declare a variable to store our result and initialize it with 1.
	int answer = 1;

	// Iterating 'N' times.
	for (int i = 1; i <= n; i++) {
		// Multiply answer with 'X' and then do modulo with 'M'.
		answer = (1LL * answer * x) % m;
	}
	// Return the answer.
	return answer;
}