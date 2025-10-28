fun main() {
    val n = readLine()!!.toInt()
    val visited = BooleanArray(n + 1) { false }
    val answer: MutableList<Int> = mutableListOf()

    fun choose(depth: Int) {
        if (depth == n) {
            println(answer.joinToString(" "))
        }

        for (num in n downTo 1) {
            if (visited[num]) continue

            answer.add(num)
            visited[num] = true
            choose(depth + 1)
            answer.removeLast()
            visited[num] = false
        }
    }

    choose(0)
}