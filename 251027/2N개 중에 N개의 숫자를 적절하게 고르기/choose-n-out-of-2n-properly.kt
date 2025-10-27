import kotlin.math.abs

fun main() {
    val n = readLine()!!.toInt()
    val nums = readLine()!!.split(" ").map { it.toInt() }
    val sumOfNums = nums.sum()

    var answer = sumOfNums

    fun dfs(start: Int, num: Int, depth: Int) {
        if (answer == 0) return

        if (depth == n) {
            val diff = abs((sumOfNums - num) - num)
            if (diff < answer) answer = diff
            return
        }

        for (i in start until nums.size) {
            val targetNum = nums[i]
            dfs(i + 1, num + targetNum, depth + 1)
        }
    }

    dfs(0, 0, 0)

    println(answer)
}