import kotlin.math.abs

fun main() {
    val n = readLine()!!.toInt()
    val grid = List(n) { readLine()!! }

    var start = Pair(-1, -1)
    var end = Pair(-1, -1)
    val coinPositions: MutableList<Triple<Int, Int, Int>> = mutableListOf()

    for (i in grid.indices) {
        for (j in grid[i].indices) {
            when {
                grid[i][j] == 'S' -> start = Pair(j, i)
                grid[i][j] == 'E' -> end = Pair(j, i)
                grid[i][j].isDigit() -> coinPositions.add(Triple(grid[i][j].digitToInt(), j, i))
            }
        }
    }

    var answer = Int.MAX_VALUE

    fun getDistanceFromHere(fromX: Int, fromY: Int, toX: Int, toY: Int): Int {
        return abs(fromX - toX) + abs(fromY - toY)
    }

    // 동전을 3개 모으기 전까지는 동전의 위치로 이동
    // 동전을 3개 모았다면 E 좌표로 이동
    // 동전은 번호가 증가하는 순서대로 수집
    fun dfs(
        x: Int,
        y: Int, 
        move: Int, 
        coinCount: Int, 
        lastCoinNumber: Int,
    ) {
        // 코인 3개 수집 시 도착점으로 이동
        if (coinCount == 3) {
            val distanceToEndPoint = getDistanceFromHere(x, y, end.first, end.second)
            answer = minOf(answer, move + distanceToEndPoint)
            return
        }

        for (coinPosition in coinPositions) {
            val (coinNumber, coinX, coinY) = coinPosition
            if (coinNumber <= lastCoinNumber) continue

            if (9 - coinNumber >= 3 - coinCount) {
                val distanceToCoin = getDistanceFromHere(x, y, coinX, coinY)
                dfs(coinX, coinY, move + distanceToCoin, coinCount + 1, coinNumber)
            }
        }
    }

    dfs(start.first, start.second, 0, 0, 0)

    if (answer == Int.MAX_VALUE) {
        println(-1)
    } else {
        println(answer)
    }
}