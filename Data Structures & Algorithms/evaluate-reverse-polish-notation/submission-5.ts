class Solution {
    /**
     * @param {string[]} tokens
     * @return {number}
     */
    evalRPN(tokens: string[]): number {
        const stack: number[] = [];
        for( const token of tokens) {

            const num = Number(token);

            if (!Number.isNaN(num)) {
                stack.push(num);
            } else {
                const val1 = stack.pop();
                const val2 = stack.pop();
                let res = 0;
                if (token == '+') {
                    res = val2 + val1;
                } else if (token == '-') {
                    res = val2 - val1;
                } else if (token == '*') {
                    res = val2 * val1;
                } else {
                    res = Math.trunc(val2 / val1);
                }
                stack.push(res);
            }
        }
        return stack.pop();
    }
}


