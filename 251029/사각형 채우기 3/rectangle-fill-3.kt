fun main() {
    val n = readLine()!!.toInt()
    val dp = IntArray(n + 1) { 0 }

    dp[0] = 1
    dp[1] = 2

    for (i in 2 until n + 1) {
        dp[i] = (dp[i - 1] * 2 + dp[i - 2] * 3) % 10007
        for (j in i - 3 downTo 0) {
            dp[i] = (dp[i] + dp[j] * 2) % 10007
        }
    }

    println(dp[n])
}