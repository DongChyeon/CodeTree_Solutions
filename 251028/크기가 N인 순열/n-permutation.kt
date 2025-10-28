fun main() {
    val n = readLine()!!.toInt()

    val visited = BooleanArray(n + 1) { false }
    val answer: MutableList<Int> = mutableListOf()

    fun choose(depth: Int) {
        if (depth == n) {
            println(answer.joinToString(" "))
            return
        }
        
        for (num in 1 until n + 1) {
            if (visited[num]) continue

            visited[num] = true
            answer.add(num)
            choose(depth + 1)
            visited[num] = false
            answer.removeLast()        
        } 
    }

    choose(0)
}