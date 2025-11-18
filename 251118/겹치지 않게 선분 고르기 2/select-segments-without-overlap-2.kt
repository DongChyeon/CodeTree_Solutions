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
    var minX2 = segments[0].second
    for (i in 1 until n) {
        if (segments[i].first > minX2) {
            answer += 1
            minX2 = segments[i].second
        }
    }

    println(answer)
}