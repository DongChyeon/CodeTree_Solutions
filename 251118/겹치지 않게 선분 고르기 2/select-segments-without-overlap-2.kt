fun main() {
    val n = readLine()!!.toInt()
    val segments = Array(n) {
        val (x1, x2) = readLine()!!.trim().split(" ").map { it.toInt() }
        Pair(x1, x2)
    }
    segments.sortWith(
        compareBy<Pair<Int, Int>> { it.second }
    )

    var answer = 1
    for (i in 1 until n) {
        val (x1, x2) = segments[0]
        val (nx1, nx2) = segments[i]

        if (nx1 > x2) answer += 1
    }

    println(answer)
}