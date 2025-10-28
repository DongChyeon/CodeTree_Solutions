import java.util.Queue
import java.util.LinkedList

fun main() {
    val (n, m) = readLine()!!.trim().split(" ").map { it.toInt() }
    val grid = Array(n) { readLine()!!.trim().split(" ").map { it.toInt() }.toIntArray() }
    val visited = Array(n) { BooleanArray(m) { false } }

    val dirs = listOf(0 to -1, 0 to 1, -1 to 0, 1 to 0)

    fun isInRange(x: Int, y: Int) : Boolean {
        return x in 0 until m && y in 0 until n
    }
    
    // 녹인 얼음 반환
    fun melt(startX: Int, startY: Int) : MutableSet<Pair<Int, Int>> {
        val queue: Queue<Pair<Int, Int>> = LinkedList()
        queue.add(Pair(startX, startY))
        visited[startY][startX] = true

        var meltedIces = mutableSetOf<Pair<Int, Int>>()

        while (queue.isNotEmpty()) {
            // 주변 얼음 녹이기
            val (x, y) = queue.poll()
            for ((dx, dy) in dirs) {
                val (nx, ny) = Pair(x + dx, y + dy)
                if (isInRange(nx, ny) && grid[ny][nx] == 1) {
                    meltedIces.add(Pair(nx, ny))
                }

                if (isInRange(nx, ny) && grid[ny][nx] == 0 && !visited[ny][nx]) {
                    queue.add(Pair(nx, ny))
                    visited[ny][nx] = true
                }
            }
        }

        return meltedIces
    }

    var remainCount = grid.sumOf { row -> row.count { it == 1 } }
    var (startX, startY) = Pair(0, 0)

    for (time in 1 until 201) {
        val meltedIces = melt(startX, startY)
        for ((x, y) in meltedIces) grid[y][x] = 0

        startX = meltedIces.first().first
        startY = meltedIces.first().second

        remainCount -= meltedIces.size

        if (remainCount == 0) {
            println("$time ${meltedIces.size}")
            return
        }
    }
}