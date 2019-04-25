<div class="section" id="scipy-ndimage-imread">
<h1>scipy.ndimage.imread<a class="headerlink" href="#scipy-ndimage-imread" title="Permalink to this headline">¶</a></h1>
<dl class="function">
<dt id="scipy.ndimage.imread">
<tt class="descclassname">scipy.ndimage.</tt><tt class="descname">imread</tt><big>(</big><em>fname</em>, <em>flatten=False</em>, <em>mode=None</em><big>)</big><a class="reference external" href="http://github.com/scipy/scipy/blob/v0.17.0/scipy/ndimage/io.py#L22-L28"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#scipy.ndimage.imread" title="Permalink to this definition">¶</a></dt>
<dd><p>Read an image from a file as an array.</p>
<table class="docutils field-list" frame="void" rules="none">
<colgroup><col class="field-name">
<col class="field-body">
</colgroup><tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><p class="first"><strong>fname</strong> : str or file object</p>
<blockquote>
<div><p>The file name or file object to be read.</p>
</div></blockquote>
<p><strong>flatten</strong> : bool, optional</p>
<blockquote>
<div><p>If True, flattens the color layers into a single gray-scale layer.</p>
</div></blockquote>
<p><strong>mode</strong> : str, optional</p>
<blockquote>
<div><p>Mode to convert image to, e.g. <tt class="docutils literal"><span class="pre">'RGB'</span></tt>.  See the Notes for more
details.</p>
</div></blockquote>
</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body"><p class="first"><strong>imread</strong> : ndarray</p>
<blockquote class="last">
<div><p>The array obtained by reading the image.</p>
</div></blockquote>
</td>
</tr>
</tbody>
</table>
<p class="rubric">Notes</p>
<p><a class="reference internal" href="#scipy.ndimage.imread" title="scipy.ndimage.imread"><tt class="xref py py-obj docutils literal"><span class="pre">imread</span></tt></a> uses the Python Imaging Library (PIL) to read an image.
The following notes are from the PIL documentation.</p>
<p><em class="xref py py-obj">mode</em> can be one of the following strings:</p>
<ul class="simple">
<li>‘L’ (8-bit pixels, black and white)</li>
<li>‘P’ (8-bit pixels, mapped to any other mode using a color palette)</li>
<li>‘RGB’ (3x8-bit pixels, true color)</li>
<li>‘RGBA’ (4x8-bit pixels, true color with transparency mask)</li>
<li>‘CMYK’ (4x8-bit pixels, color separation)</li>
<li>‘YCbCr’ (3x8-bit pixels, color video format)</li>
<li>‘I’ (32-bit signed integer pixels)</li>
<li>‘F’ (32-bit floating point pixels)</li>
</ul>
<p>PIL also provides limited support for a few special modes, including
‘LA’ (‘L’ with alpha), ‘RGBX’ (true color with padding) and ‘RGBa’
(true color with premultiplied alpha).</p>
<p>When translating a color image to black and white (mode ‘L’, ‘I’ or
‘F’), the library uses the ITU-R 601-2 luma transform:</p>
<div class="highlight-python" style="position: relative;"><div class="highlight"><pre><span></span><span class="n">L</span> <span class="o">=</span> <span class="n">R</span> <span class="o">*</span> <span class="mi">299</span><span class="o">/</span><span class="mi">1000</span> <span class="o">+</span> <span class="n">G</span> <span class="o">*</span> <span class="mi">587</span><span class="o">/</span><span class="mi">1000</span> <span class="o">+</span> <span class="n">B</span> <span class="o">*</span> <span class="mi">114</span><span class="o">/</span><span class="mi">1000</span>
</pre></div>
</div>
<p>When <em class="xref py py-obj">flatten</em> is True, the image is converted using mode ‘F’.
When <em class="xref py py-obj">mode</em> is not None and <em class="xref py py-obj">flatten</em> is True, the image is first
converted according to <em class="xref py py-obj">mode</em>, and the result is then flattened using
mode ‘F’.</p>
</dd></dl>

</div>