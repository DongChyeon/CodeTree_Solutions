import kotlin.math.min

fun main() {
    val n = readLine()!!.trim().toInt()
    val cost = Array(n) { 
        readln().trim().split(" ").map { it.toInt() }
    }

    // 0-based Index (출발점을 0으로)
    val choosedPlaces: MutableList<Int> = mutableListOf(0)
    val visited = BooleanArray(n) { false }

    var answer = Int.MAX_VALUE

    fun getCost(): Int {
        var result = 0

        for (i in 0 until choosedPlaces.size - 1) {
            val prevPlace = choosedPlaces[i]
            val curPlace = choosedPlaces[i + 1]

            result += cost[prevPlace][curPlace]
        }

        result += cost[choosedPlaces.last()][0]

        return result
    }

    fun choose(depth: Int) {
        if (depth == n) {
            if (cost[choosedPlaces.last()][0] != 0) {
                answer = min(answer, getCost())
            }
            return
        }

        for (i in 1 until n) {
            val lastPlace = choosedPlaces.last() ?: 0
            if (visited[i] || cost[lastPlace][i] == 0) continue

            choosedPlaces.add(i)
            visited[i] = true
            choose(depth + 1)
            choosedPlaces.removeLast()
            visited[i] = false
        }

    }

    choose(1)

    println(answer)
}