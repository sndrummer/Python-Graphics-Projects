<div class="show-content user_content clearfix enhanced">
  <h1 class="page-title">Useful Numpy Commands</h1>
  
<p>You may find the following Numpy functions helpful as you complete the labs in CS355:</p>
<table style="width: 769px;">
<tbody>
<tr>
<td style="width: 207px;"><a href="https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.linspace.html" class="external" target="_blank" rel="noreferrer noopener"><span><span>np.linspace(start,stop,num)</span><span class="screenreader-only">&nbsp;(Links to an external site.)</span></span><span class="ui-icon ui-icon-extlink ui-icon-inline" title="Links to an external site."><span class="screenreader-only">Links to an external site.</span></span></a></td>
<td style="width: 550px;">Returns a Numpy array of size&nbsp;<em>num</em> with evenly spaced values between&nbsp;<em>start</em> and&nbsp;<em>stop</em>.</td>
</tr>
<tr>
<td style="width: 207px;"><a href="https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.ndarray.shape.html" class="external" target="_blank" rel="noreferrer noopener"><span><span>arr.shape</span><span class="screenreader-only">&nbsp;(Links to an external site.)</span></span><span class="ui-icon ui-icon-extlink ui-icon-inline" title="Links to an external site."><span class="screenreader-only">Links to an external site.</span></span></a></td>
<td style="width: 550px;">Returns a tuple of the size of each dimension in a Numpy array.</td>
</tr>
<tr>
<td style="width: 207px;"><a href="https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.zeros.html" class="external" target="_blank" rel="noreferrer noopener"><span><span>np.zeros(arr.shape)</span><span class="screenreader-only">&nbsp;(Links to an external site.)</span></span><span class="ui-icon ui-icon-extlink ui-icon-inline" title="Links to an external site."><span class="screenreader-only">Links to an external site.</span></span></a></td>
<td style="width: 550px;">Returns a new Numpy array of zeros of the same shape as&nbsp;<em>arr</em>. This is great for making buffer images.</td>
</tr>
<tr>
<td style="width: 207px;"><a href="https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.array.html" class="external" target="_blank" rel="noreferrer noopener"><span><span>np.array(list)</span><span class="screenreader-only">&nbsp;(Links to an external site.)</span></span><span class="ui-icon ui-icon-extlink ui-icon-inline" title="Links to an external site."><span class="screenreader-only">Links to an external site.</span></span></a></td>
<td style="width: 550px;">Turns a standard Python list into a Numpy array.</td>
</tr>
<tr>
<td style="width: 207px;"><a href="https://docs.scipy.org/doc/numpy-1.13.0/reference/arrays.indexing.html" class="external" target="_blank" rel="noreferrer noopener"><span><span>arr[start:stop:step,...,...]</span><span class="screenreader-only">&nbsp;(Links to an external site.)</span></span><span class="ui-icon ui-icon-extlink ui-icon-inline" title="Links to an external site."><span class="screenreader-only">Links to an external site.</span></span></a></td>
<td style="width: 550px;">Returns the portion of&nbsp;<em>arr</em> described by standard Python slice notation. Commas separate slice notation for each dimension.&nbsp;A single colon returns every element of the specified dimension.</td>
</tr>
<tr>
<td style="width: 207px;"><a href="https://docs.scipy.org/doc/numpy-1.13.0/user/basics.broadcasting.html" class="external" target="_blank" rel="noreferrer noopener"><span><span>arr + number&nbsp;</span><span class="screenreader-only">&nbsp;(Links to an external site.)</span></span><span class="ui-icon ui-icon-extlink ui-icon-inline" title="Links to an external site."><span class="screenreader-only">Links to an external site.</span></span></a></td>
<td style="width: 550px;">
<p>Performs the element-wise addition of each element of&nbsp;<em>arr&nbsp;</em>with&nbsp;<em>number</em>. This also works with subtraction(-), multiplication(*), division(/) and others.</p>
</td>
</tr>
<tr>
<td style="width: 207px;"><a href="https://docs.scipy.org/doc/numpy-1.13.0/user/basics.broadcasting.html" class="external" target="_blank" rel="noreferrer noopener"><span><span>arr1 + arr2</span><span class="screenreader-only">&nbsp;(Links to an external site.)</span></span><span class="ui-icon ui-icon-extlink ui-icon-inline" title="Links to an external site."><span class="screenreader-only">Links to an external site.</span></span></a></td>
<td style="width: 550px;">
<p>Performs the element-wise addition between&nbsp;<em>arr1&nbsp;</em>with <i>arr2</i>. This also works with subtraction(-), multiplication(*), division(/) and others.&nbsp;<strong>Warning:&nbsp; &nbsp; </strong>If&nbsp;<em>arr1&nbsp;</em>and&nbsp;<em>arr2</em> are both matrices, * performs a matrix multiplication.</p>
</td>
</tr>
<tr>
<td style="width: 207px;"><a href="https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.multiply.html" class="external" target="_blank" rel="noreferrer noopener"><span><span>np.multiply(arr1,arr2)</span><span class="screenreader-only">&nbsp;(Links to an external site.)</span></span><span class="ui-icon ui-icon-extlink ui-icon-inline" title="Links to an external site."><span class="screenreader-only">Links to an external site.</span></span></a></td>
<td style="width: 550px;">Returns the element-wise multiplication of&nbsp;<em>arr1&nbsp;</em>and&nbsp;<em>arr2.</em>
</td>
</tr>
<tr>
<td style="width: 207px;"><a href="https://docs.scipy.org/doc/numpy-dev/reference/generated/numpy.matmul.html" class="external" target="_blank" rel="noreferrer noopener"><span><span>np.matmul(arr1, arr2)</span><span class="screenreader-only">&nbsp;(Links to an external site.)</span></span><span class="ui-icon ui-icon-extlink ui-icon-inline" title="Links to an external site."><span class="screenreader-only">Links to an external site.</span></span></a></td>
<td style="width: 550px;">Returns the matrix multiplication&nbsp;<em>arr1&nbsp;</em>and&nbsp;<em>arr2.</em>
</td>
</tr>
<tr>
<td style="width: 207px;"><a href="https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.dot.html" class="external" target="_blank" rel="noreferrer noopener"><span><span>np.dot(arr1, arr2)</span><span class="screenreader-only">&nbsp;(Links to an external site.)</span></span><span class="ui-icon ui-icon-extlink ui-icon-inline" title="Links to an external site."><span class="screenreader-only">Links to an external site.</span></span></a></td>
<td style="width: 550px;">Returns the dot product of&nbsp;<em>arr1&nbsp;</em>and&nbsp;<em>arr2</em>.&nbsp;<strong>Warning:</strong> Make sure that&nbsp;<em>arr1&nbsp;</em>and&nbsp;<em>arr2</em> are both row vectors or both column vectors.</td>
</tr>
<tr>
<td style="width: 207px;"><a href="https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.cross.html" class="external" target="_blank" rel="noreferrer noopener"><span><span>np.cross(arr1, arr2)</span><span class="screenreader-only">&nbsp;(Links to an external site.)</span></span><span class="ui-icon ui-icon-extlink ui-icon-inline" title="Links to an external site."><span class="screenreader-only">Links to an external site.</span></span></a></td>
<td style="width: 550px;">
<span>Returns the cross product of&nbsp;</span><em>arr1&nbsp;</em><span>and&nbsp;</span><em>arr2</em><span>.&nbsp;</span><strong>Warning:</strong><span>&nbsp;Make sure that&nbsp;</span><em>arr1&nbsp;</em><span>and&nbsp;</span><em>arr2</em><span>&nbsp;are both row vectors or both column vectors.</span>
</td>
</tr>
<tr>
<td style="width: 207px;"><a href="https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.sum.html" class="external" target="_blank" rel="noreferrer noopener"><span><span>np.sum(arr, axis=None)</span><span class="screenreader-only">&nbsp;(Links to an external site.)</span></span><span class="ui-icon ui-icon-extlink ui-icon-inline" title="Links to an external site."><span class="screenreader-only">Links to an external site.</span></span></a></td>
<td style="width: 550px;">Sums all elements in a Numpy array. If you specify an axis, it will only sum along that axis.</td>
</tr>
<tr>
<td style="width: 207px;"><a href="https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.atleast_2d.html" class="external" target="_blank" rel="noreferrer noopener"><span><span>np.atleast_2D(arr)</span><span class="screenreader-only">&nbsp;(Links to an external site.)</span></span><span class="ui-icon ui-icon-extlink ui-icon-inline" title="Links to an external site."><span class="screenreader-only">Links to an external site.</span></span></a></td>
<td style="width: 550px;">Turns a 1D list into a 2D Numpy matrix array.</td>
</tr>
<tr>
<td style="width: 207px;"><a href="https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.ndarray.T.html" class="external" target="_blank" rel="noreferrer noopener"><span><span>arr.T</span><span class="screenreader-only">&nbsp;(Links to an external site.)</span></span><span class="ui-icon ui-icon-extlink ui-icon-inline" title="Links to an external site."><span class="screenreader-only">Links to an external site.</span></span></a></td>
<td style="width: 550px;">If&nbsp;<em>arr</em> is 2D, it returns the matrix transpose.</td>
</tr>
<tr>
<td style="width: 207px;"><a href="https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.amax.html" class="external" target="_blank" rel="noreferrer noopener"><span><span>np.amax(arr, axis=None)</span><span class="screenreader-only">&nbsp;(Links to an external site.)</span></span><span class="ui-icon ui-icon-extlink ui-icon-inline" title="Links to an external site."><span class="screenreader-only">Links to an external site.</span></span></a></td>
<td style="width: 550px;">Returns the maximum value of a Numpy array. If you specify an axis, it will return each maximum value along that axis.</td>
</tr>
<tr>
<td style="width: 207px;"><a href="https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.argmax.html" class="external" target="_blank" rel="noreferrer noopener"><span><span>np.argmax(arr, axis=None)</span><span class="screenreader-only">&nbsp;(Links to an external site.)</span></span><span class="ui-icon ui-icon-extlink ui-icon-inline" title="Links to an external site."><span class="screenreader-only">Links to an external site.</span></span></a></td>
<td style="width: 550px;">Returns the index of the maximum value of a Numpy array. If you specify an axis, it will return the index of each maximum value along that axis.</td>
</tr>
<tr>
<td style="width: 207px;"><a href="https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.clip.html" class="external" target="_blank" rel="noreferrer noopener"><span><span>np.clip(arr, min, max)</span><span class="screenreader-only">&nbsp;(Links to an external site.)</span></span><span class="ui-icon ui-icon-extlink ui-icon-inline" title="Links to an external site."><span class="screenreader-only">Links to an external site.</span></span></a></td>
<td style="width: 550px;">Returns an array where each element is between min and max.</td>
</tr>
</tbody>
</table>
  
</div>