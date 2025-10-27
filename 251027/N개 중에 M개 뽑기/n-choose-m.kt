fun main() {
    val (n, m) = readLine()!!.split(" ").map { it.toInt() }

    fun dfs(start: Int, path: MutableList<Int>) {
        if (path.size == m) {
            println(path.joinToString(" "))
        }
        for (i in start until n + 1) {
            path.add(i)
            dfs(i + 1, path)
            path.removeLast()
        }
    }

    dfs(1, mutableListOf())
}
