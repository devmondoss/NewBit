import PDFKit
let a = CommandLine.arguments
let d = PDFDocument(url: URL(fileURLWithPath: a[1]))!
var out = ""
for i in 0..<d.pageCount { out += "\n<!-- pág. PDF \(i+1) -->\n" + (d.page(at: i)?.string ?? "") + "\n" }
try! out.write(toFile: a[2], atomically: true, encoding: .utf8)
