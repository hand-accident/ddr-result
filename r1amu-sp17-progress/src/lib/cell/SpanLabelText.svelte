<script>
    let className;
    export { className as class };
</script>

<span class="c {className}">
    <slot />
</span>

<style lang="postcss" module>
    .c {
        @apply label-text;
    }
</style>
