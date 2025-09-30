def greetUser(name) {
    return "Hello, ${name}!"
}

def calculateSum(a, b) {
    return a + b
}

def formatDate(date) {
    return date.format('yyyy-MM-dd')
}

def isEmptyString(str) {
    return str == null || str.trim().isEmpty()
}

def logMessage(message) {
    println "[INFO] ${message}"
}