import kotlin.math.max

fun main() {
    val n = readLine()!!.trim().toInt()
    val sequence = readln().trim().split(" ").map { it.toInt() }
    val dp = IntArray(n) { 1 }

    for (i in 1 until n) {
        var maxLength = 0

        for (j in 0 until i) {
            if (sequence[i] > sequence[j]) {
                dp[i] = max(dp[i], dp[j] + 1)
            }
        }
    }

    //println(dp.joinToString(" "))
    println(dp.maxOrNull()!!)
}