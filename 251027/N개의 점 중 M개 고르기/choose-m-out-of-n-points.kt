import kotlin.math.pow

fun main() {
    val (n, m) = readln().split(" ").map { it.toInt() }
    val points = List(n) {
        val (x, y) = readln().split(" ").map { it.toInt() }
        Pair(x, y)
    }
    val selectedPoints: MutableList<Pair<Int, Int>> = mutableListOf()

    var answer = Int.MAX_VALUE

    fun getDistance(point1: Pair<Int, Int>, point2: Pair<Int, Int>): Int {
        val result = (point1.first - point2.first).toDouble().pow(2) + (point1.second - point2.second).toDouble().pow(2)
        return result.toInt()
    }

    fun getMaxDistance(points: List<Pair<Int, Int>>): Int {
        var maxDistance = 0

        for (i in 0 until points.size - 1) {
            for (j in i + 1 until points.size) {
                val distance = getDistance(points[i], points[j])
                if (distance > maxDistance) {
                    maxDistance = distance
                }
            }
        }

        return maxDistance
    }

    fun dfs(start: Int, count: Int) {
        if (count == m) {
            val result = getMaxDistance(selectedPoints)
            if (answer > result) answer = result
            return
        }

        for (i in start until points.size) {
            selectedPoints.add(points[i])
            dfs(i + 1, count + 1)
            selectedPoints.removeLast()
        }
    }

    dfs(0, 0)

    println(answer)
}