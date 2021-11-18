# github-banner

Use the github contributions activity summary to make art. Inspired from
a [blog post][post] of [Bastian Venthur][venthur].

[post]: https://venthur.de/2020-12-30-streak.html
[venthur]: https://github.com/venthur

## How it works

The contribution activity summary has 7 rows for the days of week and 52
columns for the weeks of the year. Since the first and last week can be
incomplete, we draw in the 7x50 area in the middle. There are 4 shades of
activity, which are mapped to the unicode blocks ░, ▒, ▓ and █ in
[banner.txt](banner.txt).

## Related stuff

I discovered the more advanced [gitfitti][gitfitti] after writing this
code. Be sure to check it out!

[gitfitti]: https://github.com/diffractometer/gitfitti
