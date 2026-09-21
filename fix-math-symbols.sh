#!/bin/bash
# ============================================================
# Convert Unicode subscripts/superscripts to HTML <sub>/<sup>
# for maximum cross-device compatibility (fixes □ boxes)
# ============================================================

set -e

echo "🔄 Converting math symbols in lesson files..."

# Find every lesson HTML file
find entrance-exam paths foundations -type f -path '*/lessons/*.html' 2>/dev/null | while read file; do
  echo "  Processing: $file"

  # Backup
  cp "$file" "$file.bak"

  # Subscript digits 0-9
  sed -i 's/₀/<sub>0<\/sub>/g' "$file"
  sed -i 's/₁/<sub>1<\/sub>/g' "$file"
  sed -i 's/₂/<sub>2<\/sub>/g' "$file"
  sed -i 's/₃/<sub>3<\/sub>/g' "$file"
  sed -i 's/₄/<sub>4<\/sub>/g' "$file"
  sed -i 's/₅/<sub>5<\/sub>/g' "$file"
  sed -i 's/₆/<sub>6<\/sub>/g' "$file"
  sed -i 's/₇/<sub>7<\/sub>/g' "$file"
  sed -i 's/₈/<sub>8<\/sub>/g' "$file"
  sed -i 's/₉/<sub>9<\/sub>/g' "$file"

  # Subscript letters (common in math)
  sed -i 's/ₐ/<sub>a<\/sub>/g' "$file"
  sed -i 's/ₑ/<sub>e<\/sub>/g' "$file"
  sed -i 's/ₕ/<sub>h<\/sub>/g' "$file"
  sed -i 's/ᵢ/<sub>i<\/sub>/g' "$file"
  sed -i 's/ⱼ/<sub>j<\/sub>/g' "$file"
  sed -i 's/ₖ/<sub>k<\/sub>/g' "$file"
  sed -i 's/ₗ/<sub>l<\/sub>/g' "$file"
  sed -i 's/ₘ/<sub>m<\/sub>/g' "$file"
  sed -i 's/ₙ/<sub>n<\/sub>/g' "$file"
  sed -i 's/ₒ/<sub>o<\/sub>/g' "$file"
  sed -i 's/ₚ/<sub>p<\/sub>/g' "$file"
  sed -i 's/ᵣ/<sub>r<\/sub>/g' "$file"
  sed -i 's/ₛ/<sub>s<\/sub>/g' "$file"
  sed -i 's/ₜ/<sub>t<\/sub>/g' "$file"
  sed -i 's/ᵤ/<sub>u<\/sub>/g' "$file"
  sed -i 's/ᵥ/<sub>v<\/sub>/g' "$file"
  sed -i 's/ₓ/<sub>x<\/sub>/g' "$file"

  # Subscript plus/minus/equals/parens
  sed -i 's/₊/<sub>+<\/sub>/g' "$file"
  sed -i 's/₋/<sub>-<\/sub>/g' "$file"
  sed -i 's/₌/<sub>=<\/sub>/g' "$file"
  sed -i 's/₍/<sub>(<\/sub>/g' "$file"
  sed -i 's/₎/<sub>)<\/sub>/g' "$file"

  # Superscript digits
  sed -i 's/⁰/<sup>0<\/sup>/g' "$file"
  sed -i 's/¹/<sup>1<\/sup>/g' "$file"
  sed -i 's/²/<sup>2<\/sup>/g' "$file"
  sed -i 's/³/<sup>3<\/sup>/g' "$file"
  sed -i 's/⁴/<sup>4<\/sup>/g' "$file"
  sed -i 's/⁵/<sup>5<\/sup>/g' "$file"
  sed -i 's/⁶/<sup>6<\/sup>/g' "$file"
  sed -i 's/⁷/<sup>7<\/sup>/g' "$file"
  sed -i 's/⁸/<sup>8<\/sup>/g' "$file"
  sed -i 's/⁹/<sup>9<\/sup>/g' "$file"

  # Superscript letters and symbols
  sed -i 's/ⁿ/<sup>n<\/sup>/g' "$file"
  sed -i 's/ⁱ/<sup>i<\/sup>/g' "$file"
  sed -i 's/⁺/<sup>+<\/sup>/g' "$file"
  sed -i 's/⁻/<sup>-<\/sup>/g' "$file"
  sed -i 's/⁼/<sup>=<\/sup>/g' "$file"
  sed -i 's/⁽/<sup>(<\/sup>/g' "$file"
  sed -i 's/⁾/<sup>)<\/sup>/g' "$file"
done

echo ""
echo "✅ Done. Backups saved as *.bak"
echo ""
echo "Preview changes:"
find entrance-exam paths foundations -type f -path '*/lessons/*.html.bak' 2>/dev/null | head -3 | while read bak; do
  orig="${bak%.bak}"
  echo "  diff $orig:"
  diff "$bak" "$orig" | head -10 || true
done
