pkgname=quote
pkgver=1.0
pkgrel=1
pkgdesc="A simple CLI tool that prints a random quote"
arch=('any')
url="https://github.com/sankarlmao/quote-cli"
license=('sankarlmao')
depends=('python')
source=("$pkgname::git+https://github.com/sankarlmao/quote-cli.git")
md5sums=('SKIP')

package() {
    cd "$srcdir/$pkgname"
    install -Dm755 quote "$pkgdir/usr/bin/quote"
}
