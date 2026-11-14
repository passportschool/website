#!/usr/bin/env bash
U="https://passportschool.web-f67.workers.dev"
echo '=== ROUTES ==='
for p in "" "parents-2/school-calendar/" "students-2/grading-scale/" "faculty-and-staff/" "admin/"; do
  printf '%-34s ' "/$p"
  curl -sS -o /dev/null -w '%{http_code}\n' --max-time 20 "$U/$p"
done
echo '=== 404 HANDLING ==='
curl -sS -o /dev/null -w '%{http_code}\n' --max-time 20 "$U/nope-doesnt-exist"
echo '=== LEGACY 301s (critical) ==='
curl -sS -o /dev/null -w '/parents-2/ -> %{http_code} %{redirect_url}\n' --max-time 20 "$U/parents-2/"
curl -sS -o /dev/null -w '/students-2/ -> %{http_code} %{redirect_url}\n' --max-time 20 "$U/students-2/"
echo '=== TITLE ==='
curl -sS --max-time 20 "$U/" 2>/dev/null | grep -oE '<title>[^<]+</title>' | head -1
echo '=== ASSET SAMPLE ==='
ASSET=$(curl -sS --max-time 20 "$U/" 2>/dev/null | grep -oE '/_astro/[A-Za-z0-9_.-]+\.(webp|avif)' | head -1)
if [ -n "$ASSET" ]; then
  curl -sS -o /dev/null -w "$ASSET -> %{http_code} (%{size_download} bytes)\n" --max-time 30 "$U$ASSET"
else
  echo 'no _astro asset found on homepage'
fi
