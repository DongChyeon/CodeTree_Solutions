import kotlin.math.max

fun main() {
    val n = readln().trim().toInt()
    val a = readln().trim().split(" ").map { it.toInt() }

    var answer = a[0]

    val dp = IntArray(n) { 0 }
    dp[0] = a[0]

    for (i in 1 until n) {
        dp[i] = max(dp[i - 1] + a[i], a[i])
        answer = max(answer, dp[i])
    }

    println(answer)
}