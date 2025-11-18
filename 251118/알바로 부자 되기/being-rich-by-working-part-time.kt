import kotlin.math.max

fun main() {
    val n = readLine()!!.toInt()
    val jobs = MutableList(n) {
        val (s, e, p) = readln().split(" ").map { it.toInt() }
        Triple(s, e, p)
    }
    
    val dp = IntArray(n)
    for (i in 0 until n) dp[i] = jobs[i].third

    for (i in 1 until n) {
        for (j in 0 until i) {
            if (jobs[i].first > jobs[j].second) {
                dp[i] = max(dp[i], dp[j] + jobs[i].third)
            }
        }
    }

    println(dp.maxOrNull()!!)
}