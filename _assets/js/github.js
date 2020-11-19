$(function () {
  var GITHUB_PROXY_BASE = "https://plugins.octoprint.org/proxy";

  window.githubStar = function (repo) {
    var url = GITHUB_PROXY_BASE + "/user/starred/" + repo;
    return $.ajax({
      url: url,
      method: "PUT",
      xhrFields: {
        withCredentials: true,
      },
      crossDomain: true,
      cache: false,
    }).fail(function (xhr, status, error) {
      if (xhr.status === 401) {
        window.githubLogin();
      }
    });
  };
  window.githubUnstar = function (repo) {
    var url = GITHUB_PROXY_BASE + "/user/starred/" + repo;
    return $.ajax({
      url: url,
      method: "DELETE",
      xhrFields: {
        withCredentials: true,
      },
      crossDomain: true,
      cache: false,
    }).fail(function (xhr, status, error) {
      if (xhr.status === 401) {
        window.githubLogin();
      }
    });
  };
  window.githubRepo = function (repo) {
    var url = GITHUB_PROXY_BASE + "/repos/" + repo;
    return $.ajax({
      url: url,
      method: "GET",
      xhrFields: {
        withCredentials: true,
      },
      crossDomain: true,
      cache: false,
    });
  };
  window.githubStatus = function (repo) {
    var url = GITHUB_PROXY_BASE + "/user/starred/" + repo;
    var deferred = $.Deferred();
    $.ajax({
      url: url,
      method: "GET",
      xhrFields: {
        withCredentials: true,
      },
      crossDomain: true,
      cache: false,
    })
      .done(function (response) {
        // logged in and starred
        deferred.resolve(true);
      })
      .fail(function (xhr, status, error) {
        if (xhr.status === 404) {
          // logged in and not starred
          deferred.resolve(false);
        } else if (xhr.status === 401) {
          // not logged in
          deferred.reject();
        }
      });
    return deferred.promise();
  };
  window.githubUser = function () {
    return $.ajax({
      url: GITHUB_PROXY_BASE + "/user",
      method: "GET",
      xhrFields: {
        withCredentials: true,
      },
      crossDomain: true,
      cache: false,
    });
  };
  window.githubLogin = function () {
    var deferred = $.Deferred();
    var win = window.open(
      GITHUB_PROXY_BASE + "/login",
      "githubLoginWindow",
      "menubar=no,toolbar=no,location=no,status=no,resizable=yes,scrollbars=yes,width=500,height=800",
      true
    );

    var checkClosed = function () {
      if (win.closed) {
        clearInterval(timer);
        window
          .githubUser()
          .done(function (response) {
            deferred.resolve(response);
          })
          .fail(function () {
            deferred.reject();
          });
        return null;
      }
    };
    var timer = setInterval(checkClosed, 100);
    return deferred.promise();
  };
  window.githubLogout = function () {
    return $.ajax({
      url: GITHUB_PROXY_BASE + "/logout",
      method: "POST",
      xhrFields: {
        withCredentials: true,
      },
      crossDomain: true,
      cache: false,
    });
  };
});
