var nersc_is_down = false;
var _cols, _i_ID, _i_ra, _i_dec, _has_mark, _delimiter, _scale, _size, _layer, _source;

const search_params = (new URL(document.location.href)).searchParams;
const _use_dev = search_params.has("dev") ? "-dev" : "";
const _do_rand_rot = search_params.has("randrot");
var _select_layer = search_params.get("layer");
if (!_select_layer && $("#layer > option[value='" + _select_layer + "']").length == 0) _select_layer = false;

/* When NERSC is down
(function(){
  var t = new Date().getTime();
  var t_out = Date.parse('9 Jul 2021 10:00:00 PDT');
  var t_back = Date.parse('12 Jul 2021 20:00:00 PDT');
  if ((t >= t_out) && (t < t_back)){
    nersc_is_down = true;
    $("span.warning").show();
  }
})();
*/

const _image_urls = {
  "desi": "https://www.legacysurvey.org/viewer" + _use_dev + "/cutout.jpg?ra=${ra}&dec=${dec}&pixscale=${scale}&layer=${layer}&size=180",
  "sdss": "https://skyserver.sdss.org/dr17/SkyServerWS/ImgCutout/getjpeg?ra=${ra}&dec=${dec}&scale=${scale}&width=180&height=180",
  "dss": "https://archive.stsci.edu/cgi-bin/dss_search?v=${layer}&r=${ra}&d=${dec}&e=J2000&h=${size}&w=${size}&f=gif",
  "merian": "https://tigress-web.princeton.edu/~jiaxuanl/Merian/cutout_RGB/magellan_cosmos_${img_id}_HSC_N708.png"
};

const _link_urls = {
  "desi": "https://www.legacysurvey.org/viewer" + _use_dev + "?ra=${ra}&dec=${dec}&layer=${layer}&zoom=14",
  "merian": "https://www.legacysurvey.org/viewer" + _use_dev + "?ra=${ra}&dec=${dec}&layer=${layer}&zoom=14",
  "sdss": "https://skyserver.sdss.org/dr17/VisualTools/navi?ra=${ra}&dec=${dec}",
  "desi-alt": "https://viewer.legacysurvey.org/?ra=${ra}&dec=${dec}&layer=${layer}&zoom=14",
  "dss": "https://archive.stsci.edu/cgi-bin/dss_search?v=${layer}&r=${ra}&d=${dec}&e=J2000&h=15&w=15&f=gif"
};

const _img_dom_template = "<img class='pic ${marked} ${rot}' title='${title}' src='${img_url}' width='180' height='180'/>";
const _linked_img_template = "<figure><a class='plink' href='${link_url}'>${img_dom}</a><figcaption>${img_caption}</a></figcaption></figure>";
const _rot_classes = ["", "r1", "r2", "r3", "r0f", "r1f", "r2f", "r3f"];
const _default_layer = $("#default-layer").attr("value");

const escapeHtml = function(s) {
  return s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
}

const loadFile = function(filePath) {
  var result = null;
  var xmlhttp = new XMLHttpRequest();
  xmlhttp.open("GET", filePath, false);
  xmlhttp.send();
  if (xmlhttp.status==200) {
    result = xmlhttp.responseText;
  }
  return result;
}

const parseHeader = function(line_raw) {
  const line = line_raw.trim();
  var has_header = true;

  _delimiter = /\s+/;
  if (line.search(",") > -1) _delimiter = ",";
  _cols = line.split(_delimiter).map(col => col.trim());

  const _cols_lower = _cols.map(col => col.toLowerCase());

  for (const key of ["id", "index", "ind", "idx", "indices", "viz-id"]) {
    _i_ID = _cols_lower.indexOf(key);
    if (_i_ID > -1) break;
  }
  for (const key of ["ra", "r.a.", "radeg", "ra2000", "right ascension", "r"]) {
    _i_ra = _cols_lower.indexOf(key);
    if (_i_ra > -1) break;
  }
  for (const key of ["dec", "decl", "decl.", "dedeg", "de2000", "declination", "de", "d"]) {
    _i_dec = _cols_lower.indexOf(key);
    if (_i_ra > -1) break;
  }

  if (_i_ra == -1 || _i_dec == -1){  // no header
    if (_cols_lower[_cols.length-1] == "true" || _cols_lower[_cols.length-1] == "false"){
      _has_mark = true;
      _cols.pop();
    }
    if (_cols.length == 2){
      _i_ra = 0;
      _i_dec = 1;
    }
    else if (_cols.length > 2){
      _i_ID = 0;
      _i_ra = 1;
      _i_dec = 2;
    }
    else{
      _has_mark = false;
      $("#list").html("<p>Error! \nPlease make sure the first line is header, and it contains at least \"ra\" and \"dec\". \nOnly supports space/tab/comma-separated tables.</p>");
      return -1;
    }
    _cols = _cols.fill("");
    has_header = false;
  }
  else{  // has header
    if (_cols_lower[_cols.length-1] == "marked"){
      _has_mark = true;
      _cols.pop();
    }
    else{
      _has_mark = false;
    }
  }
  return has_header;
};

const addImage = function(line) {
  if (!line.replace(/[-=\s]/g, "")) return;
  var items, out, mark;
  items = line.trim().split(_delimiter);
  if (_has_mark) mark = (items.pop().trim().toLowerCase() == "true");
  out = _linked_img_template
       .replace("${img_dom}", _img_dom_template)
       .replace("${link_url}", _link_urls[_source])
       .replace("${img_url}", _image_urls[_source])
       .replace("${img_id}", items[_i_ID])
       .replace(/\${ra}/g, parseFloat(items[_i_ra]).toString())
       .replace(/\${dec}/g, parseFloat(items[_i_dec]).toString())
       .replace(/\${scale}/g, _scale)
       .replace(/\${size}/g, _size)
       .replace(/\${layer}/g, _layer)
       .replace("${title}", items.map((item, i) => (_cols[i] + " = " + item.trim())).join("\n"))
       .replace("${img_caption}", _cols[_i_ID] + "=" + items[_i_ID])
       .replace("${marked}", mark ? "marked" : "")
       .replace("${rot}", _do_rand_rot ? _rot_classes[Math.floor(Math.random()*_rot_classes.length)] : "");
  $(out).appendTo(document.getElementById("list"));
};

const run = function() {
  window.stop();
  record_output();

  const current_layer = _layer;
  const current_source = _source;
  const current_size = _size;
  const current_scale = _scale;

  const layer_source = $("#layer").val().split(":");
  _layer = layer_source[0] || _default_layer;
  _source = layer_source[1] || "desi";
  _size = parseFloat($("#scale").val()).toFixed(7).replace(/0+$/, '');
  _scale = (parseFloat($("#scale").val()) / 3).toFixed(7).replace(/0+$/, '');
  if (!layer_source[0]) $("#default-layer").prop("selected", true);

  const _file_path = $("#catdir").val().replace("/tigress/jiaxuanl/public_html/", "/~jiaxuanl/")
  const _input_from_file = ($("#input_source").val() == "file");

  if ((current_source != _source) || (!current_layer) || (!current_scale) || (!current_size) || $(".pic").length == 0){
    if (_input_from_file){
      var lines = escapeHtml(loadFile(_file_path)).trim().split(/\n/);
      $("#input").val(escapeHtml(loadFile(_file_path)).trim())
    }
    
    var lines = escapeHtml($("#input").val()).trim().split(/\n/);
    
    const has_header = parseHeader(lines[0]);
    if (has_header == -1) return;
    if (has_header) lines.shift();

    $("#list").empty();
    lines.forEach(addImage);
    update_click_events();
    return;
  }

  if (current_layer == _layer && current_size == _size && current_scale == _scale) return;
  $(".pic").each((i, elem) => {
    const url = $(elem).attr("src")
                .replace("="+current_layer+"&", "="+_layer+"&")
                .replace("scale="+current_scale+"&", "scale="+_scale+"&")
                .replace("h="+current_size+"&w="+current_size, "h="+_size+"&w="+_size);
    $(elem).attr("src", url);
  });

  if (current_layer == _layer) return;
  $(".plink").each((i, elem) => {
    const url = $(elem).attr("href").replace("="+current_layer+"&", "="+_layer+"&");
    $(elem).attr("href", url);
  });
};

const update_click_events = function(){
  if ($("#enable_marking").prop("checked")){
    $(".plink").on("click", (event) => { event.preventDefault(); });
    $(".pic").on("click", (event) => {
      if (event.ctrlKey) { window.open( $(event.target).parent().attr("href") ); }
      else {
        $(event.target).toggleClass("marked");
        $("#generate_output").prop("disabled", false);
     }
    });
    $("#input").prop("readonly", true);
    $("#generate_output").addClass("pure-button-primary");
  }
  else{
    record_output();
    $(".plink, .pic").off("click");
    $("#input").prop("readonly", false);
    $("#generate_output").removeClass("pure-button-primary");
  }
};

const record_output = function(){
  if ($("#generate_output").prop("disabled") || $(".pic").length == 0) return;
  var out = _cols.join("\t") + "\tmarked\n";
  if (out.trim() == "marked") out = "";  // no header
  out += $(".pic").map((i, elem) => (
    $(elem).attr("title").split(/\n/).map(item => item.substring(item.indexOf(" = ") + 3)).join("\t")
    + "\t" + $(elem).hasClass("marked")
  )).get().join("\n");
  $("#input").val(out);
  $("#generate_output").prop("disabled", true);
}

$("form").on("submit", (event) => {event.preventDefault();});
$("#generate_output").on("click", record_output);
$("#load_cat").on("click", run);
$("#layer").on("input", run);
$("#scale").on("input", run);
$("#input").on("input", () => { _source = ""; run(); });
$("#enable_marking").on("input", () => {
  if ($(".pic").length == 0) { run(); }
  else { update_click_events() };
});
$(window).on("beforeunload", () => {
  if (!$("#generate_output").prop("disabled")){
    return "Are you sure you want to close this page? You cannot recover the marks you made!";
  }
});

if (_select_layer){ $("#layer > option[value='" + _select_layer + "']").prop("selected", true); }
if (search_params.get("input")) { $("#input").val(search_params.get("input")); }

if (_select_layer || search_params.get("input")){ run(true); }
else { document.getElementById("layer").focus(); }