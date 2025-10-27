fun main() {
    val (n, m) = readln().trim().split(" ").mapNotNull { it.toInt() }
    val numbers = readln().trim().split(" ").mapNotNull { it.toInt() }
    var answer = 0
    
    fun dfs(start: Int, path: MutableList<Int>) {
        if (path.size == m) {
            val result = path.reduce { acc, num -> acc xor num }
            if (result > answer) answer = result
            return
        }

        for (i in start until numbers.size) {
            path.add(numbers[i])
            dfs(i + 1, path)
            path.removeLast()
        }
    }

    dfs(0, mutableListOf())
    print(answer)
}