fun main() {
    val n = readLine()!!.toInt()

    if (n < 2) {
        println(1)
        return
    }

    val dp = IntArray(n + 1) { 0 }
    dp[1] = 1
    dp[2] = 2
    for (i in 3 until n + 1) {
        dp[i] = (dp[i - 1] + dp[i - 2]) % 10007
    }

    println(dp[n])
}