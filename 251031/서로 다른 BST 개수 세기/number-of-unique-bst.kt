fun main() {
    val n = readLine()!!.trim().toInt()
    val dp = IntArray(n + 1) { 0 }
    dp[0] = 1
    dp[1] = 1

    for (i in 2 until n + 1) {
        var total = 0
        for (j in 0 until i) {  // j = 루트 노드 - 1
            total += dp[j] * dp[i - j - 1]  // 왼쪽 서브 트리 (루트 노드보다 작음), 오른쪽 서브 트리 (루트 노드보다 큼)
        }
        dp[i] = total
    }

    println(dp[n])
}