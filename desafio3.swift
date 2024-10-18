print("Qual é o seu nome?")
if let nome = readLine() {
    print("Quantos anos você tem?")
    if let idadeStr = readLine(), let idade = Int(idadeStr) {
        if idade >= 18 {
            print("\(nome), você é maior de idade.")
        } else {
            print("\(nome), você é menor de idade.")
        }
    } else {
        print("Entrada inválida para a idade.")
    }
}