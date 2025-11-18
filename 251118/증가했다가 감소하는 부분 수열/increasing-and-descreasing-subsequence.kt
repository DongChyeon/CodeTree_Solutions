import kotlin.math.max

fun main() {
    val n = readLine()!!.trim().toInt()
    val arr = readLine()!!.trim().split(" ").map { it.toInt() }
    
    val dp1 = IntArray(n) { 1 }    // 증가 수열
    val dp2 = IntArray(n) { 1 }    // 감소 수열

    for (i in 1 until n) {
        for (j in 0 until i) {
            if (arr[i] > arr[j]) {
                dp1[i] = max(dp1[i], dp1[j] + 1)
            }

            if (arr[i] < arr[j]) {
                dp2[i] = max(dp2[i], dp2[j] + 1)
            }
        }
        
        dp2[i] = max(dp1[i], dp2[i])
    }

    println(dp2.maxOrNull()!!)
}