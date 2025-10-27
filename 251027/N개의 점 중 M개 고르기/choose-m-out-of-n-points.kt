import kotlin.math.sqrt
import kotlin.math.pow
import kotlin.math.abs
import kotlin.math.max
import kotlin.math.min

fun main() {
    val (n, m) = readln().split(" ").map { it.toInt() }
    val points = List(n) {
        val (x, y) = readln().split(" ").map { it.toInt() }
        Pair(x, y)
    }

    var answer = Int.MAX_VALUE

    fun getDistance(x1: Int, x2: Int, y1: Int, y2: Int) : Int {
        val result = (x1 - x2).toDouble().pow(2) + (y1 - y2).toDouble().pow(2)
        return result.toInt()
    }

    fun dfs(start: Int, count: Int, minX: Int, maxX: Int, minY: Int, maxY: Int) {
        if (count == m) {
            val result = getDistance(minX, maxX, minY, maxY)
            if (answer > result) answer = result
            return
        }

        for (i in start until points.size) {
            val (pointX, pointY) = points[i]
            dfs(i + 1, count + 1, min(minX, pointX), max(maxX, pointX), min(minY, pointY), max(maxY, pointY))
        }
    }

    dfs(0, 0, 100, 1, 100, 1)

    println(answer)
}