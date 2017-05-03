const fs = require('fs');
const gulp = require('gulp');
const gutil = require('gulp-util');
const jshint = require('gulp-jshint');
const rename = require('gulp-rename');
const path = require('path');


gulp.task('crossbar-config', callback => {
  // Copies default Crossbar configuration file to Crossbar node directory if it
  // exists.
  const crossbarConfigPath = path.join('.crossbar', 'config.yaml');
  fs.access(crossbarConfigPath, err => {
    if (err) {
      gutil.log(
        'Create default Crossbar configuration file',
        gutil.colors.cyan(crossbarConfigPath)
      );
      gulp.src('default_crossbar_config.yaml')
      .pipe(rename(path.basename(crossbarConfigPath)))
      .pipe(gulp.dest(path.dirname(crossbarConfigPath)))
      .on('end', callback);
    } else {
      gutil.log(
        'Crossbar configuration file ',
        gutil.colors.cyan(crossbarConfigPath),
        'already exists. Skip this task.'
      );
      callback();
    }
  });
});


gulp.task('default', [
  'crossbar-config'
], () => {});


gulp.task('jshint', () => {
  // Runs JSHint on our JavaScript code.
  return gulp.src('gulpfile.js')
    .pipe(jshint({esversion: 6}))
    .pipe(jshint.reporter('default'));
});
