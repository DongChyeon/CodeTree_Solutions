fun main() {
    val n = readLine()!!.toInt()
    val dp = IntArray(n + 1) { 0 }

    if (n < 2) {
        println(0)
        return
    }
    
    if (n == 2) {
        println(1)
        return
    }

    dp[1] = 0
    dp[2] = 1
    dp[3] = 1
    for (i in 4 until n + 1) {
        dp[i] = (dp[i - 2] + dp[i - 3]) % 10007
    }

    println(dp[n])
}