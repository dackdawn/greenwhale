path = ''

html_str = """
<script>
(function() {
    var OldXHR = window.XMLHttpRequest;

    function newXHR() {
        var realXHR = new OldXHR();
        realXHR.addEventListener("load", () => {
            if (realXHR.responseURL.indexOf("hasUnlock") !== -1) {
                var data = {
                    code: 0,
                    msg: "操作成功",
                    data: true
                };
                Object.defineProperty(realXHR, "responseText", {
                    writable: true
                });
                Object.defineProperty(realXHR, "response", {
                    writable: true
                });
                realXHR.response = JSON.stringify(data);
                realXHR.responseText = JSON.stringify(data);
            }
        }, false);
        return realXHR;
    };
    window.XMLHttpRequest = newXHR;
})();
</script>
"""
with open(f'{path}/index.html', 'ab') as file:
    file.write(html_str.encode('utf8'))
