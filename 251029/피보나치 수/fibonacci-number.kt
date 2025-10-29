fun main() {
    val n = readLine()!!.toInt()
    val arr = IntArray(n + 1) { 0 }
    arr[0] = 1
    arr[1] = 1
    for (i in 2 until n) {
        arr[i] = arr[i - 1] + arr[i - 2]
    }
    println(arr[n - 1])
}