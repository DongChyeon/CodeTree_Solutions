import kotlin.math.max

fun main() {
    val n = readln().trim().toInt()
    val coins = readln().trim().split(" ").map { it.toInt() }

    val dp = List(n + 1) { IntArray(4) { 0 }}

    dp[1][1] = coins[0]
    dp[2][0] = coins[1]
    dp[2][2] = dp[1][1] + coins[1]

    for (i in 3 until n + 1) {
        for (j in 0 until 4) {
            if (dp[i - 2][j] != 0) dp[i][j] = max(dp[i][j],dp[i - 2][j] + coins[i - 1])
            if (j >= 1 && dp[i - 1][j - 1] != 0) dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + coins[i - 1])
        }
    }

    println(dp[n].maxOrNull()!!)
}