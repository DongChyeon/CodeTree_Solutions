import kotlin.math.max

fun main() {
    val n = readLine()!!.trim().toInt()
    val numbers = readln().trim().split(" ").map { it.toInt() }
    val dp = IntArray(n) { 1 } 

    for (i in 1 until n) {
        for (j in 0 until i) {
            if (numbers[i] < numbers[j]) dp[i] = max(dp[i], dp[j] + 1)
        }
    }
    
    println(dp.maxOrNull()!!)
}