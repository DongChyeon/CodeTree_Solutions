import kotlin.math.max

fun main() {
    val n = readLine()!!.trim().toInt()
    val jumpDistances = readLine()!!.trim().split(" ").map { it.toInt() }
    val dp = IntArray(n) { 0 }

    for (i in 1..jumpDistances[0]) dp[i] = 1
    for (i in 1 until n) {
        for (j in 0 until i) {
            if (jumpDistances[j] >= i - j && dp[j] != 0) dp[i] = max(dp[i], dp[j] + 1)
        }
    }

    println(dp.maxOrNull()!!)
}