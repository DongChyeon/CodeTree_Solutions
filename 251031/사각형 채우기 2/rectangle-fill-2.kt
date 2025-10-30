fun main() {
    val n = readLine()!!.trim().toInt()
    val dp = IntArray(n + 1) { 0 }
    dp[0] = 1
    dp[1] = 1

    for (i in 2 until n + 1) {
        dp[i] = (dp[i - 1] + 2 * dp[i - 2]) % 10007
    }

    println(dp[n])
}