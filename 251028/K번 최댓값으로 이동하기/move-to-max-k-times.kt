import java.util.Queue
import java.util.LinkedList

fun main() {
    val (n, k) = readln().trim().split(" ").map { it.toInt() }
    val grid = Array(n) { readln().trim().split(" ").map { it.toInt() } }
    val (r, c) = readln().trim().split(" ").map { it.toInt() }
    
    val dirs = listOf(0 to -1, 0 to 1, -1 to 0, 1 to 0)

    fun isInRange(x: Int, y: Int): Boolean {
        return x in 0 until n && y in 0 until n
    }

    fun bfs(startX: Int, startY: Int): Pair<Int, Int> {
        val startNumber = grid[startY][startX]
        var (nextX, nextY) = -1 to -1

        val visited = Array(n) { BooleanArray(n) { false } }
        val queue: Queue<Pair<Int, Int>> = LinkedList()
        visited[startY][startX] = true
        queue.add(startX to startY)

        while (queue.isNotEmpty()) {
            val (x, y) = queue.poll()

            // 시작점이 아닌 경우
            if (grid[y][x] != startNumber) {
                if (nextX == -1 && nextY == -1) {
                    nextX = x
                    nextY = y
                } else if (grid[y][x] == grid[nextY][nextX]) {
                    // 행 번호가 가장 작은 곳
                    if (y < nextY) {
                        nextX = x
                        nextY = y
                    // 행 번호가 같다면 열 번호가 가장 작은 곳
                    } else if (y == nextY && x < nextX) {
                        nextX = x
                        nextY = y
                    }
                } else if (grid[y][x] > grid[nextY][nextX]) {
                    nextX = x
                    nextY = y
                }
            }

            for ((dx, dy) in dirs) {
                val (nx, ny) = x + dx to y + dy

                if (isInRange(nx, ny) && !visited[ny][nx] && grid[ny][nx] < startNumber) {
                    visited[ny][nx] = true
                    queue.add(nx to ny)
                }
            }
        }

        return Pair(nextX, nextY)
    }
    
    var (startX, startY) = c - 1 to r - 1
    var (endX, endY) = c - 1 to r - 1
    repeat(k) {
        val (nx, ny) = bfs(startX, startY)
        endX = nx
        endY = ny
        //println("${grid[endY][endX]} ${endY + 1} ${endX + 1}")

        if (startX == endX && startY == endY) {
            println("${endY + 1} ${endX + 1}")
            return
        }

        startX = endX
        startY = endY
    }

    println("${endY + 1} ${endX + 1}")
}