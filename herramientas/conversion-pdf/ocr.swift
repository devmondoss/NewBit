import PDFKit
import Vision
import AppKit
// uso: ocr <pdf> <desde> <hasta> <salida.md>
let a = CommandLine.arguments
let d = PDFDocument(url: URL(fileURLWithPath: a[1]))!
let desde = Int(a[2])!, hasta = min(Int(a[3])!, d.pageCount)
var out = ""
for i in (desde-1)..<hasta {
  autoreleasepool {
    let p = d.page(at: i)!; let r = p.bounds(for: .mediaBox); let sc: CGFloat = 2.5
    let w = Int(r.width*sc), h = Int(r.height*sc)
    let cs = CGColorSpaceCreateDeviceRGB()
    let ctx = CGContext(data: nil, width: w, height: h, bitsPerComponent: 8, bytesPerRow: 0, space: cs, bitmapInfo: CGImageAlphaInfo.noneSkipLast.rawValue)!
    ctx.setFillColor(CGColor(red: 1, green: 1, blue: 1, alpha: 1)); ctx.fill(CGRect(x: 0, y: 0, width: w, height: h))
    ctx.scaleBy(x: sc, y: sc); p.draw(with: .mediaBox, to: ctx)
    let img = ctx.makeImage()!
    let req = VNRecognizeTextRequest()
    req.recognitionLevel = .accurate; req.recognitionLanguages = ["es-ES", "en-US"]; req.usesLanguageCorrection = true
    try! VNImageRequestHandler(cgImage: img).perform([req])
    let obs = (req.results ?? []).sorted { a, b in
      let ya = a.boundingBox.midY, yb = b.boundingBox.midY
      if abs(ya - yb) > 0.008 { return ya > yb }; return a.boundingBox.minX < b.boundingBox.minX }
    let lines = obs.compactMap { $0.topCandidates(1).first?.string }
    out += "\n<!-- pág. PDF \(i+1) -->\n" + lines.joined(separator: "\n") + "\n"
    FileHandle.standardError.write("\(i+1) ".data(using: .utf8)!)
  }
}
try! out.write(toFile: a[4], atomically: true, encoding: .utf8)
