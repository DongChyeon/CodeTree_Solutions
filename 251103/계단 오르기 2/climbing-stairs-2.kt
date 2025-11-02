import kotlin.math.max

fun main() {
    val n = readln().trim().toInt()
    val coins = readln().trim().split(" ").map { it.toInt() }

    val dp = List(n + 1) { IntArray(4) { 0 }}

    for (i in 1 until n + 1) {
        for (j in 1 until 4) {
            dp[i][j] = dp[i - 1][j - 1] + coins[i - 1]
            if (i > 1) dp[i][j] = max(dp[i][j], dp[i - 2][j] + coins[i - 2])
        }
    }

    println(dp[n].maxOrNull()!!)
}