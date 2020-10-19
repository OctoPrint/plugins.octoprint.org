$(function() {
    // YouTube embeds with consent
    var embeds = document.getElementsByClassName("yt-with-consent");
    for (var i = 0; i < embeds.length; i++) {
        var embed = embeds[i];
        var vid = embed.dataset.vid;
        if (!vid) continue;

        var preview = embed.dataset.preview || "/assets/img/yt-with-consent/" + vid + ".jpg";
        embed.style.backgroundImage = "url(" + preview + ")";
        embed.style.backgroundSize = "contain";
        embed.style.backgroundRepeat = "no-repeat";
        embed.style.backgroundPosition = "center";
        embed.style.backgroundColor = "black";

        var button = document.createElement("div");
        button.classList.add("play-button");
        button.onclick = function () {
            var iframe = document.createElement("iframe"),
                url = "https://www.youtube-nocookie.com/embed/" + this.parentNode.dataset.vid + "?autoplay=1&rel=0";
            iframe.setAttribute("src", url);
            iframe.setAttribute("frameborder", "0");
            iframe.setAttribute("allowfullscreen", "1");
            this.parentNode.parentNode.replaceChild(iframe, this.parentNode);
        };
        embed.appendChild(button);

        var disclaimer = document.createElement("div");
        disclaimer.classList.add("yt-disclaimer");
        disclaimer.innerHTML = "This video will be embedded from Youtube. The <a href='https://policies.google.com/privacy?hl=en' rel='noreferrer noopener' target='_blank'>Privacy Policies of Google</a> apply.";
        embed.appendChild(disclaimer);
    }
});