import kotlin.math.max

fun main() {
    val (n, m) = readln().trim().split(" ").map { it.toInt() }
    val grid = Array(n) { readln().trim().split(" ").map { it.toInt() }.toIntArray() }
    val dp = Array(n) { IntArray(m) { -1 } }
    dp[0][0] = 1

    for (i in 1 until n) {
        for (j in 1 until m) {
            for (y in 0 until i) {
                for (x in 0 until j) {
                    if (grid[y][x] == -1) continue
                    if (grid[i][j] > grid[y][x]) dp[i][j] = max(dp[i][j], dp[y][x] + 1)
                }
            }
        }
    }
    
    //for (row in dp) println(row.joinToString(" "))
    println(dp.map { it.toList() }.flatten().maxOrNull()!!)
}